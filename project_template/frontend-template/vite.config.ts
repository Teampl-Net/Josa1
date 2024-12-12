import type { ConfigEnv } from "vite";
import { VueConfig } from "@teampl-net/vite-config-custom";

// https://vitejs.dev/config/
export default (viteConfigEnv: ConfigEnv) => {
  return VueConfig(viteConfigEnv);
};
