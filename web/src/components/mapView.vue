<template>
  <div>
    <v-bottom-sheet v-model="sheet" class="floating-menu" scrollable>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          class="mx-2 floating-menu"
          fab
          dark
          large
          bottom
          right
          color="red"
          v-bind="attrs"
          v-on="on"
        >
          <v-icon dark>mdi-pencil</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-text style="height: 70%;">
          <v-list>
            <v-subheader>線を編集</v-subheader>
            <v-list two-line>
            <template v-for="(drawingRailroad, index) in drawingRailroads">
              <railroad-selector
                  :drawingRailroad="drawingRailroad"
                  :operatingCompanies="operatingCompanies"
                  :key="drawingRailroad.id"
                  @deleteRailroad="deleteRailroad"
                ></railroad-selector>
              <v-divider v-if="index + 1 < drawingRailroads.length" :key="index+10000"
              ></v-divider>
            </template>
            </v-list>
            <div class="add-button">
              <v-btn dark large color="green" @click="addRailroad">
                <v-icon dark left>mdi-plus</v-icon>追加する
              </v-btn>
            </div>
            <v-divider />
            <v-subheader>保存する</v-subheader>
            <div class="add-button">
              <v-btn dark large color="blue" @click="save">
                <v-icon dark left>mdi-floppy</v-icon>画像として保存
              </v-btn>
            </div>
          </v-list>
        </v-card-text>
      </v-card>
    </v-bottom-sheet>

    <l-map
      ref="map"
      id="mappreview"
      class="mapPane"
      :zoom="zoom"
      :center="center"
      :options="options"
    >
      <!-- <l-tile-layer
        :visible="true"
        url="https://tile.thunderforest.com/transport/{z}/{x}/{y}.png?apikey=80f270976fbb4096a6a5115a6348bd15"
        attribution="Data <a href='https://www.openstreetmap.org/copyright'>© OpenStreetMap contributors</a>"
        layer-type="base"
      ></l-tile-layer> -->
      <l-tile-layer
        :visible="true"
        url="https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="Data <a href='https://www.openstreetmap.org/copyright'>© OpenStreetMap contributors</a>"
        layer-type="base"
      ></l-tile-layer>
      <!--      <l-tile-layer-->
      <!--        :visible="true"-->
      <!--        url="http://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png"-->
      <!--        layer-type="overlay"-->
      <!--      ></l-tile-layer>-->
      <l-geo-json
        v-for="drawingRailroad in drawingRailroads"
        :geojson="drawingRailroad.geojson"
        :options="drawingRailroad.options"
        v-bind:key="drawingRailroad.id"
      ></l-geo-json>
    </l-map>
  </div>
</template>

<script>
import L from "leaflet";
import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet";

import "leaflet-easyprint";
import RailroadSelector from "@/components/railroadSelector";

export default {
  name: "mapView2",
  components: {
    RailroadSelector,
    LMap,
    LTileLayer,
    LGeoJson
  },

  data() {
    return {
      center: [38, 135],
      zoom: 6,
      drawingRailroads: [],  // 描画してるやつら
      operatingCompanies: [],  // 鉄道事業者
      sheet: false,
      uid: 1,
      options: {
        useCache: true,
        zoomControl: false,
        crossOrigin: true
      }
    };
  },
  mounted() {
    this.$nextTick(function() {
      const vh = window.innerHeight * 0.01;
      document.documentElement.style.setProperty("--vh", `${vh}px`);
    });
  },
  created() {
    this.$axios.get("/railways").then(res => {
      this.operatingCompanies = res.data;
    });
  },
  methods: {
    save: function() {
      var p1080 = {
        width: 1920,
        height: 1080,
        className: "p1080class",
        tooltip: "1080p size"
      };

      const map = this.$refs.map.mapObject;
      const printPlugin = L.easyPrint({
        exportOnly: true,
        sizeModes: [p1080],
        hidden: true,
        tileLayer: L.tileLayer(
          "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
        ),
        tileWait: 500
      }).addTo(map);
      printPlugin.printMap("p1080class", "MyManualPrint");
    },

    addRailroad: function() {
      this.drawingRailroads.push({
        id: this.uid++,
        // name: "",
        startStation: {
          stationname: '',
          id: ''
        },
        endStation: {
          stationname: '',
          id: ''
        },
        geojson: null,
        stations: [],
        railway: {
          name: '',
          id: ''
        },
        options: {
          onEachFeature: (feature, layer) => {
            layer.options.smoothFactor = 2;
          },
          style: function style() {
            return {
              weight: 4,
              color: "#0000FF",
              fillOpacity: 0.3
            };
          }
        }
      });
    },
    deleteRailroad: function(toDeleteId) {
      const toDeleteIdx = this.drawingRailroads.findIndex(
        line => line.id === toDeleteId
      );
      this.drawingRailroads.splice(toDeleteIdx, 1);
    }
  }
};
</script>

<style scoped>
.mapPane {
  height: calc(var(--vh, 1vh) * 100 - 64px);
  margin: 0;
  text-align: left;
}
.floating-menu {
  z-index: 999;
  position: absolute;
  right: 1%;
  top: calc((var(--vh, 1vh) * 100) - 110px - 64px);
}
.add-button {
  z-index: 999;
  position: relative;
  display: inline-block;
  top: 50%;
  left: 50%;
  transform: translateX(-50%);
  margin-top: 20px;
  margin-bottom: 20px;
}

.easyPrintHolder .p1080class {
  background-image: url(data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTguMS4xLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDQ0NC44MzMgNDQ0LjgzMyIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgNDQ0LjgzMyA0NDQuODMzOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgd2lkdGg9IjUxMnB4IiBoZWlnaHQ9IjUxMnB4Ij4KPGc+Cgk8Zz4KCQk8cGF0aCBkPSJNNTUuMjUsNDQ0LjgzM2gzMzQuMzMzYzkuMzUsMCwxNy03LjY1LDE3LTE3VjEzOS4xMTdjMC00LjgxNy0xLjk4My05LjM1LTUuMzgzLTEyLjQ2N0wyNjkuNzMzLDQuNTMzICAgIEMyNjYuNjE3LDEuNywyNjIuMzY3LDAsMjU4LjExNywwSDU1LjI1Yy05LjM1LDAtMTcsNy42NS0xNywxN3Y0MTAuODMzQzM4LjI1LDQzNy4xODMsNDUuOSw0NDQuODMzLDU1LjI1LDQ0NC44MzN6ICAgICBNMzcyLjU4MywxNDYuNDgzdjAuODVIMjU2LjQxN3YtMTA4LjhMMzcyLjU4MywxNDYuNDgzeiBNNzIuMjUsMzRoMTUwLjE2N3YxMzAuMzMzYzAsOS4zNSw3LjY1LDE3LDE3LDE3aDEzMy4xNjd2MjI5LjVINzIuMjVWMzR6ICAgICIgZmlsbD0iIzAwMDAwMCIvPgoJPC9nPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+Cjwvc3ZnPgo=);
}
</style>
