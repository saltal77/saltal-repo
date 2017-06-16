import React, { Component } from 'react';
import ContainerMenu from './../components/ContainerMenu'
import ContainerFooter from './../components/footer'


export default class Blog extends Component {


    // componentDidMount()
    // {
    //     //alert("Добро Пожаловать!")
    //     let welcomeWin = window.open("Hello:welcome", "hello", "width=350,height=100");
    //
    //     let welcome = '<div class="col-md-11"><h3>Добро пожаловать на сайт!</h3></div>';
    //
    //     let wlcStyle = '<script type="text/javascript" src="vendors.js"></script><link rel="stylesheet" href="../css/style.css">';
    //
    //     welcomeWin.document.write(wlcStyle, welcome);
    // }

    render(){
        return (
            <div className="container">
                <ContainerMenu />
                <div className="row">
                    {this.props.children}
                </div>
                <ContainerFooter />
            </div>
        );
    }
}





