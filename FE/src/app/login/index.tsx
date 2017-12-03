import * as React from 'react'


interface Props {
    successHandler: ()=>void;
    cancelHandler: ()=>void;
}

interface State {
}

export default class LoginComponent extends React.Component<Props, State> {

    constructor(p: Props){
        super(p);
    }

    render(){
        return (
            <div>
                <div></div>
                <div>
                    <div>x</div>
                </div>
                <div>
                    <div>
                        <div>手机号:</div>
                        <div><input/></div>
                    </div>
                    <div>
                        <div>图片验证码:</div>
                        <div><input/></div>
                    </div>
                    <div>
                        <div>短信验证码:</div>
                        <div><input/></div>
                    </div>
                </div>
                <div>
                    <div>确定</div>
                </div>
            </div>
        )
    }
}
