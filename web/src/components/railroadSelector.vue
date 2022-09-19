<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <template v-slot:activator="{ on, attrs }">
      <v-list-item v-bind="attrs" v-on="on">
        <v-row class="my-n3">
          <v-col cols="12" class="text--secondary">
              <v-row no-gutters style="width: 100%">
                <v-col cols="12" md="5" lg="5" xl="5"
                  >路線: {{ drawingRailroad.railway.name || "未指定" }}</v-col
                >
                <v-col cols="6" md="3" lg="3" xl="3"
                  >始点: {{ drawingRailroad.startStation.station_name || "未指定" }}</v-col
                >
                <v-col cols="6" md="3" lg="3" xl="3"
                  >終点: {{ drawingRailroad.endStation.station_name || "未指定" }}</v-col
                >
              </v-row>
          </v-col>
        </v-row>
      <v-row justify="end">
        <v-btn color="error" class="mr-4" @click="deleteRailroadEmit">
          <v-icon class="pr-6" dark right>mdi-delete</v-icon>
          削除
        </v-btn>
      </v-row>
      </v-list-item>
    </template>
    <v-card>
      <v-card-title>
        <span class="headline">線路を描く</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row class="mb-n6">
            <v-col cols="12" md="12" lg="12" xl="12">
              <v-autocomplete
                  v-model="drawingRailroad.railway"
                  :items="operatingCompanies"
                  item-text="name"
                  :return-object="true"
                  label="路線名"
                  @change="onSelectRailway"
                  outlined
              ></v-autocomplete>
            </v-col>
          </v-row>
          <v-row class="my-n6">
            <v-col justify="center" cols="12" md="6" lg="6" xl="6">
              <v-autocomplete
                  v-model="drawingRailroad.startStation"
                  :items="drawingRailroad.stations"
                  item-text="station_name"
                  return-object
                  @change="onSelectStation"
                  label="始点"
                  outlined
              ></v-autocomplete>
            </v-col>
            <v-col justify="center" cols="12" md="6" lg="6" xl="6">
              <v-autocomplete
                  v-model="drawingRailroad.endStation"
                  :items="drawingRailroad.stations"
                  item-text="station_name"
                  :return-object="true"
                  label="終点"
                  @change="onSelectStation"
                  outlined
              ></v-autocomplete>
            </v-col>
          </v-row>
          <v-row justify="end" class="my-n6">
            <v-switch v-model="option" label="オプション"></v-switch>
          </v-row>
          <v-subheader v-if="option" class="mb-n6">線の太さ</v-subheader>
          <v-row v-if="option" justify="end" class="my-n6">
            <v-col cols="4">
            <v-text-field
                v-model="weight"
                type="number"
            ></v-text-field>
            </v-col>
          </v-row>
          <v-subheader v-if="option">線の色</v-subheader>
          <v-row v-if="option" justify="center">
            <v-color-picker
                v-model="color"
                elevation="2"
                mode="hexa"
            ></v-color-picker>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
        <v-btn color="blue darken-1" text @click="dialog = false; onChangeStyle()">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "railroadSelector",
  props: ["operatingCompanies", "drawingRailroad"],
  data: () => ({
    dialog: false,
    color: "#0000FF",
    weight: 4,
    option: false
  }),
  methods: {
    onSelectRailway: function() {
      // 路線選択時に
      // ・駅名データを取得
      // ・線データを取得
      // ・色データを取得
      // (TODO: まとめる)
      this.$axios
        .get(`/${this.drawingRailroad.railway.id}/stations`)
        .then(res => {
          this.drawingRailroad.stations = res.data;
          this.drawingRailroad.endStation = res.data[res.data.length - 1];
          this.drawingRailroad.startStation = res.data[0];
        })
        .then(() => {
          this.$axios
            .get(`/${this.drawingRailroad.railway.id}/geojson`, {
              params: {
                startId: this.drawingRailroad.startStation.gid,
                endId: this.drawingRailroad.endStation.gid
              }
            })
            .then(res => {
              this.drawingRailroad.geojson = res.data;
            });
        })
      this.$axios
        .get(`/${this.drawingRailroad.railway.id}/color`)
        .then(res => {
          let weight = this.weight;
          let color = res.data.color;
          this.color = color;
          this.drawingRailroad.options.style = function style() {
            return {
              weight: weight,
              color: color,
              fillOpacity: 0.3
            };
          }
      })
    },
    onSelectStation: function() {
      // 駅名選択時，
      // 線区を再取得する
      this.$axios
        .get(`/${this.drawingRailroad.railway.id}/geojson`, {
          params: {
            startId: this.drawingRailroad.startStation.gid,
            endId: this.drawingRailroad.endStation.gid
          }
        })
        .then(res => {
          this.drawingRailroad.geojson = res.data;
        });
    },
    onChangeStyle: function() {
      let weight = this.weight;
      let color = this.color;
      this.drawingRailroad.options.style = function style() {
        return {
          weight: weight,
          color: color,
          fillOpacity: 0.3
        };
      }
    },
    deleteRailroadEmit: function() {
      this.$emit("deleteRailroad", this.drawingRailroad.id);
    }
  }
};
</script>

<style scoped></style>
