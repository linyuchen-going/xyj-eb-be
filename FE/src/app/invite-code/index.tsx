import * as React from 'react'
import {ApiResInviteCode} from "../../api/user/invite-code/responses";
import {apiInviteCodes} from "../../api/user/invite-code"
import * as STYLE from './style.css'


interface State{
    codes: ApiResInviteCode[];
}

interface Props{}

export default class InviteCordsComponent extends React.Component<Props, State>{

    constructor(props: Props){
        super(props);
        this.state = {
            codes: []
        }
    }

    componentWillMount(){
        apiInviteCodes().then((codes)=>{
            this.setState({codes})
        })
    }

    render(){
        let codeEles = this.state.codes.map((code)=>{
            return (
                <div key={code.id} className={STYLE.codeItem}>
                    <div className={code.used ? STYLE.used : STYLE.unused}>
                        {code.used ? '不' : ''}可使用
                    </div>
                    <div className={STYLE.detail}>
                        <div className={STYLE.title}>
                            产品购买邀请码
                        </div>
                        <div className={STYLE.code}>
                            {code.code}
                        </div>
                        <div className={STYLE.restTime}>
                            剩余时间{code.rest_time}
                        </div>
                    </div>
                </div>
            )
        });
        return (
            <div className={STYLE.container}>
                <div className={STYLE.codeItems}>
                    {codeEles}
                </div>
            </div>
        )
    }
}