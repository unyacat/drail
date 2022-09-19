from flask import Flask, request, jsonify
import psycopg2
from waitress import serve

# DB接続情報
DB_HOST = 'db'
DB_PORT = '5432'
DB_NAME = 'drail'
DB_USER = 'postgres'
DB_PASS = 'password'


# DB接続関数
def get_connection():
    return psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'
    .format(
        user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT, dbname=DB_NAME
))


app = Flask(__name__, static_folder='./dist/static', template_folder='./dist/web')
app.config["JSON_AS_ASCII"] = False

@app.route("/railways")
def hello_world():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT array_to_json(array_agg(t.*)) FROM (
            SELECT lines.id, concat(operating_companies.name, ' ', lines.name) as name FROM lines 
            JOIN operating_companies ON operating_companies.id = lines.company_id
        ) t
    """)
    rows = cur.fetchall()[0][0]
    conn.close()
    return jsonify(rows)


@app.route("/<int:railroad_id>/stations")
def opid(railroad_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'''SELECT array_to_json(array_agg(t.*))
                FROM ( SELECT gid, station_name, geom FROM railroads 
                        WHERE line_id = {railroad_id} and station_name is not null
                        ORDER BY gid
                )t;
    ''')
    rows = cur.fetchall()[0][0]
    conn.close()
    return jsonify(rows)


@app.route("/<int:line_id>/geojson")
def geojson(line_id):
    conn = get_connection()
    cur = conn.cursor()
    if request.args.get('startId') is None or request.args.get('endId') is None:
        return "パラメータ不足", 400
    start_id = request.args.get('startId')
    end_id = request.args.get('endId')
    if end_id < start_id:
        start_id, end_id = end_id, start_id
    cur.execute(f'''SELECT json_build_object(
                        'type', 'FeatureCollection',
                        'features', json_agg(ST_AsGeoJSON(railroads.*)::json)
                    )
                    FROM railroads
                    WHERE line_id = {line_id} AND {start_id} <= gid AND gid <= {end_id}
    ''')
    rows = cur.fetchall()[0][0]
    conn.close()
    return jsonify(rows)

@app.route("/<int:line_id>/color")
def color(line_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'''SELECT color
                    FROM lines
                    WHERE id = '{line_id}'
    ''')
    rows = cur.fetchall()
    conn.close()
    return jsonify({"color": "#" + rows[0][0]})


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=3000)