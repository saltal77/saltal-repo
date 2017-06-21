import React, { Component } from 'react';
import Modal_Window from './modal';
import NavLink from './NavLink'


export default class menuNavbar extends Component {

    constructor() {
        super(...arguments);

        this.state = {
            user: ''
        };
    }

    toLogin(){

        return <Modal_Window />;
    }

    isActive(href) {
        //console.log(href);
        return window.location.pathname == href;
    }

    componentWillMount(){
        localStorage.clear();
    }

    shouldComponentUpdate() {
        let user = window.localStorage.getItem('login');
        this.setState({
            user: user
        });
        return true
    }

    render(){

        return (
            <div className="row">

                <nav className="navbar  navbar-light col-md-12">
                    <div className="container-fluid">

                        <div className="navbar-header">
                            {/*<a className={(this.isActive('/')? 'active' : '')+ " navbar-brand"} href="/" >Блоги</a>*/}
                            <NavLink to="/" className='navbar-brand' activeStyle={{ color: '#751975' }}
                                                                      onlyActiveOnIndex={true}>Блоги</NavLink>

                        </div>

                        <div className="collapse navbar-collapse">

                            <ul className="nav navbar-nav">
                                {/*<li><Link to="/about" activeStyle={{ color: '#751975' }}> Об авторах</Link></li>*/}
                                <li><NavLink to="/about" activeStyle={{ color: '#751975' }}>Об Авторах</NavLink></li>
                                <li><NavLink to="/comments" activeStyle={{ color: '#751975' }}>Комментарии</NavLink></li>
                                <li><NavLink to="/interest" activeStyle={{ color: '#751975' }}>Интересное</NavLink></li>
                                <li><NavLink to="/contacts" activeStyle={{ color: '#751975' }}>Контакты</NavLink></li>
                            </ul>

                            <button type="submit" className="btn btn-info" data-toggle="modal" data-target="#blogModal" >Войти</button>

                        </div>

                        <span className={this.state.user ? '': 'none'} >Давно не виделись ! {this.state.user}</span>
                    </div>
                </nav>

                {this.toLogin()}

            </div>
        );
    }
}


