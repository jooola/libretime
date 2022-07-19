import { createI18n } from "vue-i18n";

import en from "../locale/en.json";
import fr from "../locale/fr.json";

// Type-define the source schema
type MessageSchema = typeof en;

export default createI18n<[MessageSchema], "en" | "fr">({
  locale: "fr",
  fallbackLocale: "en",
  messages: {
    en,
    fr,
  },
});
