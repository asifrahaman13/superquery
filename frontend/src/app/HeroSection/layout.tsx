import React, { PropsWithChildren } from "react";
import HeroSection from "./HeroSection";
import FooterComponent from "./FooterComponent";

const Layout = ({ children }: PropsWithChildren) => {
  return (
    <div>
      <HeroSection />

      {children}

      <FooterComponent/>
    </div>
  );
};

export default Layout;
