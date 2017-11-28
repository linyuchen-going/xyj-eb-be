import * as React from 'react'
import * as STYLE from './style.css'
import {Product} from '../../product/detail'
import AddressSelectorComponent, {} from '../../address/select'
import {ApiResAddress as Address} from "../../../api/user/address/responses";
import {apiAddressDefault} from "../../../api/user/address/index";
import {apiProductDetail} from "../../../api/product/index";

let ICON_POSITION = require('./img/position.png');

interface Props{}
interface State{
    product: Product;
    inviteCode: string;
    showAddressSelector: boolean;
    address: Address;
}

export default class OrderConfirm extends React.Component<Props, State>{
    private productId: number;
    constructor(p: any){
        super(p);
        this.productId = p.match.params.productId;
        let product: Product = {
            id: 0,
            name: "加载中...",
            describe: ` `,
            price: 0,
            cover: ""
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
        if (!this.state.address.id){
            return alert("请先填写收货人信息");
        }
        alert("付款功能暂时未完成");
        location.href = "/#/"
    }

    componentWillMount(){
        apiAddressDefault().then((address)=>{
            this.setState({
                address
            })
        });

        apiProductDetail(this.productId).then((product)=>{
            this.setState({
                product
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
                        <input className={STYLE.inviteCode}
                               onChange={(v)=>{this.setState({inviteCode: v.target.value})}}
                               placeholder="在此填入邀请码"
                        />
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
