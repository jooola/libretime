import { resolve } from "path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vuetify from "@vuetify/vite-plugin";
import vueI18n from "@intlify/vite-plugin-vue-i18n";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vuetify({ autoImport: true }),
    vueI18n({
      include: resolve(__dirname, "./locales/**"),
    }),
  ],
});
