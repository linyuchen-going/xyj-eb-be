import * as React from 'react'
import * as STYLE from './style.css'
import {Product} from '../../product/detail'
import AddressSelectorComponent, {} from '../../address/select'
import {ApiResAddress as Address} from "../../../api/user/address/responses";
import {apiAddressDefault} from "../../../api/user/address/index";

let ICON_POSITION = require('./img/position.png');

interface Props{}
interface State{
    product: Product;
    inviteCode: string;
    showAddressSelector: boolean;
    address: Address;
}

export default class OrderConfirm extends React.Component<Props, State>{
    constructor(p: Props){
        super(p);
        let product: Product = {
            id: 0,
            name: "日本进口全球限量美容仪",
            describe: `
<img width="100%" src="http://oua8rae54.bkt.clouddn.com/test/test2.png"/>
<img width="100%" src="http://oua8rae54.bkt.clouddn.com/test/test.png"/>
`,
            price: 11000,
            first_pay_price: 0,
            cover: "http://n.sinaimg.cn/transform/20150815/Sk2_-fxfxraw8837077.jpg"
        };
        this.state = {
            product: product,
            inviteCode: "",
            showAddressSelector: false,
            address: {
                id: null,
                country: "",
                province: "",
                city: "",
                area: "",
                detail: "",
                zipcode: "",
                name: "",
                mobile: ""
            },
        }
    }

    post(){
        if(!this.state.inviteCode){
            return alert("请先填入邀请码");
        }
    }

    componentWillMount(){
        apiAddressDefault().then((address)=>{
            this.setState({
                address
            })
        })
    }


    render(){
        let {product, address} = this.state;
        
        if (this.state.showAddressSelector){
            return <AddressSelectorComponent
                btnCancelClick={()=>{this.setState({showAddressSelector: false})}}
                selectedClick={(address: Address)=>{
                    this.setState({showAddressSelector: false, address: address})
                }}/>
        }


        return (
            <div className={STYLE.confirm}>
                <div className={STYLE.addressContainer} onClick={()=>{this.setState({showAddressSelector: true})}}>
                    <div className={STYLE.iconPosition}><img src={ICON_POSITION}/></div>
                    <div className={STYLE.address}>
                        <div className={STYLE.addressPerson}>   
                            <div className={STYLE.addressReceiver}>
                                收货人：{address.name}
                            </div>
                            <div className={STYLE.addressMobile}>
                                {address.mobile}
                            </div>
                        </div>
                        <div className={STYLE.addressDetail}>
                            {address.province} {address.city} {address.area} {address.detail}
                        </div>
                    </div>
                </div>
                <div className={STYLE.order}>
                    <div className={STYLE.product}> 
                        <div className={STYLE.productCover}>
                            <img src={product.cover}/>
                        </div>
                        <div className={STYLE.productDetail}>
                            <div className={STYLE.productDetailName}>{product.name}</div>
                            <div className={STYLE.productDetailItem}>
                                <div className={STYLE.productNumTitle}>商品数量</div> <div className={STYLE.productNum}>x 1</div>
                            </div>
                            <div>
                                <div className={STYLE.productPriceTitle}>单价</div> <div className={STYLE.productPrice}>{product.price}元</div>
                            </div>
                        </div>
                    </div>

                    <div className={STYLE.orderItem}>
                        <div className={STYLE.inviteCodeTitle}>邀请码</div>
                        <input className={STYLE.inviteCode} onChange={(v)=>{this.setState({inviteCode: v.target.value})}}/>
                    </div>
                    <div>
                        <div className={STYLE.totalPaymentTitle}>金额</div>
                        <div className={STYLE.totalPayment}>{product.price}元</div>
                    </div>
                </div>
                <div className={STYLE.btnPay} onClick={()=>{this.post()}}>付款</div>
            </div>
        )
    }
}
