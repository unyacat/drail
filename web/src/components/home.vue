<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card elevation="2">
          <v-card-title class="text-h1 justify-center">
              drail
          </v-card-title>
          <v-card-subtitle class="text-h4 text-center">
            = draw + rail
          </v-card-subtitle>
          <v-card-subtitle class="text-h6 font-weight-bold">
            drailは地図上に鉄道路線を「路線・駅を選ぶだけ」で「簡単かつ正確に」描くことができるWebアプリケーションです
          </v-card-subtitle>
            <v-btn block color="pink" dark x-large class="text-h5 font-weight-bold" href="/draw">
              実際に描く
            </v-btn>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card elevation="2">
          <v-card-title class="text-h5 pb-2">
            想定用途
          </v-card-title>
          <v-card-text>
            <ul>
              <li class="text-h6">自分の旅行を記録したい時に</li>
              複雑な旅程でも正確に描くことができます
              <li class="text-h6 pt-2">動画や印刷物として配布したい時に</li>
              地図はOpenStreetMapを使用しているため著作権問題を気にする必要はありません．(ライセンス表記が必要です)
              <li class="text-h6 pt-2">線路の位置関係を確認したい時に</li>
              フリーパス等で困りがちな省略された範囲も正しい縮尺で可視化できます
            </ul>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card elevation="2">
          <v-card-title class="text-h5 pb-2">
            操作方法
          </v-card-title>
          <v-card-text>
            <ul>
              <li class="text-h6">右下の鉛筆マークを押します</li>
              <v-img
                contain
                max-height="240"
                src="@/assets/images/draw-top-arrow.png"
              >
              </v-img>
              <li class="text-h6 pt-2">線を描く</li>
              <ol>
                <li>「追加する」をクリック</li>
                <li>追加されたリストをクリック</li>
                <li>入れたい路線・線区を入力(キーボード入力可能)</li>
                <li>スクリーンショットして保存するか，「画像として保存」をクリック(現状1920x1080のみ)</li>
              </ol>
              <v-img
                contain
                max-height="240"
                src="@/assets/images/draw-lines-arrow.png"
              >
              </v-img>
            </ul>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card elevation="2">
          <v-card-title class="text-h5 pb-2">
            作例
          </v-card-title>
          <v-card-text>
            <ul>
              <li class="text-h6">都区内パス</li>
              JR東日本で発売されている「<a href="https://www.jreast.co.jp/tickets/info.aspx?GoodsCd=2485">都区内パス</a>」の実際の範囲
              <v-img
                contain
                max-height="240"
                src="@/assets/images/ex-tokunai-pass.png"
              >
              </v-img>
              <li class="text-h6">東京→福井</li>
              名古屋経由(赤)・金沢経由(青)
              <v-img
                contain
                max-height="240"
                src="@/assets/images/ex-tokyo-fukui.png"
              >
              </v-img>
            </ul>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card elevation="2">
          <v-card-title class="text-h5 pb-2">
            利用上の注意
          </v-card-title>
          <v-card-text>
            <ul>
              <li class="text-h6">ライセンスの表記</li>
              OpenStreetMapはライセンス条件下でのみ結果を配布できます．利用状況に応じて適切なクレジット表記が必要です．<a href="https://www.openstreetmap.org/copyright/">詳しく見る</a> <br />
              例えば，「© OpenStreetMap contributors」など．
              <li class="text-h6">一部の線は描画されません</li>
              できるだけ正確な線を描いていますが，処理の都合上一部線を削除しています．特に駅を並走する急行線が該当します．
            </ul>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card elevation="2">
          <v-card-title class="text-h5 pb-2">
            利用した情報
          </v-card-title>
          <v-card-text>
              <ul>
              <li><a href="https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N02-v3_0.html">国土数値情報 | 鉄道データ</a></li>
              <li><a href="https://uedayou.net/jrslod/">鉄道駅LOD - 鉄道オープンデータ提供サイト </a></li>
            </ul>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  setup() {},
});
</script>

<style scoped>
.v-application .text-h5 {
  font-weight: 600;
}
.v-application .text-h6 {
  font-weight: 600
}
.theme--light.v-card > .v-card__text {
  font-weight: 600
}
</style>
