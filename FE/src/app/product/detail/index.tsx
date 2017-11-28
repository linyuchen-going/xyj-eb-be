import * as React from 'react'
import * as STYLE from './style.css'
import * as apiProduct from '../../../api/product'
import {ApiResProductDetail, ApiResProducts} from "../../../api/product/responses";


interface Props{}
export interface Product extends ApiResProductDetail{
}

interface State{
    product: Product;
    products: Product[];
    showMoreList: boolean;
}

export default class ProductComponent extends React.Component<Props, State>{
    private productId: number | null = null;

    constructor(p: any){
        super(p);
        let product: Product = {
            id: 0,
            name: "加载中...",
            describe: ` `,
            price: 11000,
            cover: ""
        };
        this.state = {
            product: product,
            products: [product, product, product, product, product],
            showMoreList: false
        }
    }

    componentWillMount(){
        this.getAllProducts();
    }

    getProductData(id: number){
        apiProduct.apiProductDetail(id).
        then((res: ApiResProductDetail)=>{
            this.setState({
                product: res
            })
        })
    }

    getAllProducts(){
        apiProduct.apiProductList().
        then(
            (res: ApiResProducts)=>{
                this.setState({
                    products: res.results
                });
                if (!this.productId){
                    this.getProductData(res.results[0].id);
                }
            }
        )
    }

    renderMoreList(): JSX.Element{
        let products = this.state.products.map((product: Product)=>{
            return (
                <div className={STYLE.moreListProduct} key={product.id} onClick={()=>this.getProductData(product.id)}>
                    <div>
                        <img src={product.cover} />
                    </div>
                    {product.name}
                </div>
            )
        });
        if (this.state.showMoreList){
            return (
                <div className={STYLE.moreList} onClick={()=>{this.setState({"showMoreList": false})}}>
                    <div className={STYLE.moreListProducts}>
                        {products}
                    </div>
                </div>
            )
        }
        else{
            return null;
        }
    }

    render(): JSX.Element{
        let {cover, name, describe, price} = this.state.product;
        return (
            <div className={STYLE.product}>
                <div className={STYLE.cover}>
                    <img src={cover}/>
                </div>
                <div className={STYLE.content}>
                    <div className={STYLE.title}>
                        {name}
                    </div>
                    <div>
                        <div className={STYLE.star}>
                            精品推荐
                        </div>
                        <div className={STYLE.price}>
                            ￥{price}
                        </div>
                    </div>
                    <div className={STYLE.describe} dangerouslySetInnerHTML={{__html: describe}}/>
                </div>
                <div>
                    <div className={STYLE.shopBtn} onClick={()=>{location.href=`/#/order-confirm/${this.state.product.id}`}}>
                        立即购买
                    </div>
                </div>
                {this.renderMoreList()}
                {
                    !this.state.showMoreList ?
                        <div className={STYLE.moreListBtn} onClick={() => {
                            this.setState({"showMoreList": true})
                        }}>
                            更多商品>>
                        </div>
                    : null
                }
            </div>
        )
    }
}
