import React, { lazy, Suspense } from "react";
import { createBrowserHistory } from "history";
import { Router, Route, Switch } from "react-router-dom";
import "./App.css";

const HomePage = lazy(() => import("./pages/home/HomePage"));
const history = createBrowserHistory();

const App = () => {
    return (
        <Router history={history}>
            <Suspense fallback={<div>loading...</div>}>
                <Switch>
                    <Route exact path="/">
                        <HomePage />
                    </Route>
                </Switch>
            </Suspense>
        </Router>
    );
};

export default App;
