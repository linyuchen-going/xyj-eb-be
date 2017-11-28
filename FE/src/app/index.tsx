import * as React from 'react'
import * as ReactDOM from 'react-dom'
import {HashRouter, Switch, Route} from 'react-router-dom'
import ProductComponent from './product/detail'
import OrderConfirmComponent from './order/confirm'
import AddressEditComponent from './address/edit'
import AddressSelectComponent from './address/select'
import InviteCordsComponent from './invite-code'


let root = document.createElement("div");
document.body.appendChild(root);

ReactDOM.render((
    <HashRouter>
        <Switch>
            <Route path="/" exact component={ProductComponent}/>
            <Route path="/order-confirm/:productId" exact component={OrderConfirmComponent}/>
            <Route path="/address-edit" exact component={AddressEditComponent}/>
            <Route path="/address-select" exact component={AddressSelectComponent}/>
            <Route path="/invite-code" exact component={InviteCordsComponent}/>
        </Switch>
    </HashRouter>
), root);
