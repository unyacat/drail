<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app style="z-index:999">
        <v-list>
          <v-list-item link href="/">
            <v-list-item-action>
              <v-icon>mdi-home</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>ホーム</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link href="/draw">
            <v-list-item-action>
              <v-icon>mdi-pencil</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>描く</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <template v-slot:append>
          <v-list dense>
            <v-list-item link href="https://forms.gle/78rsz4BV14xpME7o8">
              <v-list-item-action>
                <v-icon>mdi-email-fast-outline</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>要望フォーム</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item link href="https://github.com/unyacat/drail">
              <v-list-item-action>
                <v-icon>mdi-github</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>unyacat/drail</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item link href="https://twitter.com/unya_2/">
              <v-list-item-action>
                <v-icon>mdi-twitter</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Made by @unya_2</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </template>
      </v-navigation-drawer>

      <v-app-bar app color="#7289DA" dark>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
        <v-toolbar-title>路線お絵描き「drail」</v-toolbar-title>
      </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data(){
    return {
      drawer: false
    }

  },
};
</script>
