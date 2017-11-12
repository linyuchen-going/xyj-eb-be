import * as React from 'react'
import * as ReactDOM from 'react-dom'
import {HashRouter, Switch, Route} from 'react-router-dom'
import ProductComponent from './product/detail'


let root = document.createElement("div");
document.body.appendChild(root);

ReactDOM.render((
    <HashRouter>
        <Switch>
            <Route path="/" exact component={ProductComponent}/>
        </Switch>
    </HashRouter>
), root);
