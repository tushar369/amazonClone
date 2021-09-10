import React, { useState } from "react";
import { Switch, Route } from "react-router-dom";
import Homepage from "./components/homepage/Homepage";
import Login from "./components/accounts/Login";

const App = () => {
  return (
    <>
      <Switch>
        <Route exact path="/" component={Homepage} />
        <Route path="/accounts" component={Login} />
      </Switch>
    </>
  );
};

export default App;
