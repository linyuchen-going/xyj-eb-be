import * as React from 'react'
import * as STYLE from './style.css'

interface Props{}
interface Product{
    id: number;
    name: string;
    describe: string;
    price: number;
    first_pay_price: number;
    cover: string;
}

interface State{
    product: Product;
    products: Product[];
    showMoreList: boolean;
}

export default class ProductComponent extends React.Component<Props, State>{
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
            products: [product, product, product, product, product],
            showMoreList: true
        }
    }

    renderMoreList(): JSX.Element{
        let products = this.state.products.map((product: Product)=>{
            return (
                <div className={STYLE.moreListProduct} key={product.id}>
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
                    <div className={STYLE.shopBtn}>
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
