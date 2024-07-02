import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/pages/**/*.{js,ts,jsx,tsx,mdx}", "./src/components/**/*.{js,ts,jsx,tsx,mdx}", "./src/app/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        "Purple-Grad-Dark-900": "#6244D6",
        "Purple-Grad-Dark-500": "#2B6CE1",
      },
      backgroundColor: {
        "Option-Background":"#2B6CE1",
        "Mustard":"#EFB023",
        "Deep-Purple":"#6244D6",
        "Almost-White":"#FCFCFC",
        "Login-Sidebar-Background": "#FFDF00",
        "Terms": "#DAA520",
        "Pri-Dark": "#333333",
        "otp_input": "#ECECEC",
        "Signup-input-color": "#F4F4F4",
        "Sidebar-Background-color": "#FFFBE0",
        "Building-button": "#F4F4F4",
        "Ready-button": "#FFF298",
        "Collecting-button": "#BCFFBC",
        "Paused-button": "#FFD1BE",
        "Neutral": "#F4F4F4",
        "Coral": "#FFA07A",
        "Lt-gray": "#EDEDED",
        "Background": "#F5F5F5",
        "Golden": "#DAA520",
        "Cross": "#C0C0C01A",
        "Golden-yellow": "#FFDF00",
        "Yellow-Tag": "#FFF298",
        "Almost-white": "#FCFCFC",
        "Bg-Gray": "#F8F8F8",
        "Accent-Blue": "#00529B",
        "Result-bg": "#F5F5F4",
        "Repondent-bg": "#F5F5F5",
        "single-choice":"#FFEFCB",
        "Lt-Aqua":"#CFEDED",
        "Save-Blue":"#2B6CE1",
        "Sec-Amber":"#EC765F",
        "Lt-Purple":"#E5E6FF",
        "Lime-Green":"#DFF4E6",
        "Footer-Dark":"#17222F"
      },
      textColor: {
        "Aqua-Dark":"#136B80",
        "Golden": "#DAA520",
        "Pri-Dark": "#333",
        "Dark-gray": "#868686",
        "Neutral-shade": "#9A9FA5",
        "Sec-Amber": "#E97451",
        "Accent-Blue": "#00529B",
        "Normal-Blue":"#2B6CE1",
        "Lt-Dark-Gray":"#868686",
        "Lt-Gray":"#C0C0C0"
      },
      borderColor: {
        "Purple-Border": "#2B6CE1",
        "Pri-Dark": "#333",
        "Gray-Background":"#F5F5F5"
      },

      fontFamily: {
        inter: ["Inter", "sans-serif"],
        sans: ["Roboto Condensed", "sans-serif"],
      },
      borderWidth: {
        s: "1px",
      },
      fontSize: {
        exsm:['12px', '20px'],
        msm: ['13px', '24px'],
        sm: ['14px', '20px'],
        base: ['14px', '24px'],
        medium: ['15px', '24px'],
        lg: ['17px', '28px'],
        exlg: ['22px', '32px'],
        xl:['28px', '48px'],
      }
    },
  },
  plugins: [],
};
export default config;
