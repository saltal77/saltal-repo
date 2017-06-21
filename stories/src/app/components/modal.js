import React, { Component } from 'react';
import axios from 'axios';
import _ from 'lodash';


export default class Modal extends Component
{

    constructor() {
        super(...arguments);
        this.checkLogin = this.checkLogin.bind(this);
    }

    checkLogin(e) {
        e.preventDefault();
        localStorage.clear();
        let login = e.target.elements[0].value;
        let pass = e.target.elements[1].value;
        let users = [];
        let allow;

        axios
            .get('../data/users_data.json')
            //.get('http://localhost:8888/store/listusers')
            .then((responce) => {
                let { data } = responce;
                users = data;
                allow = _.find(users,{user: login, pass: pass});
                if(allow){
                    window.localStorage.setItem('login', login);
                    this.context.router.push('/welcome');
                }
            });

        $('#loginForm')[0].reset();
        $('#blogModal').attr({
                'style': 'display: none',
                'class': 'modal fade'
        });
        $('body').attr({
            'style': '',
            'class': ''
        });
        $( ".modal-backdrop" ).remove();
    }

    render()
    {
        let divStyleModalContent = {
            backgroundColor: '#F3FAFE',
            backgroundImage: 'linear-gradient(90deg, transparent 79px, #E59898 79px, #E59898 81px, transparent 81px), linear-gradient(#eee .1em, transparent .1em)',
            backgroundSize: '100% 1.2em',
        };

        let h4StyleModalTitle = {
            fontFamily: "'Pangolin', cursive",
            color: '#0c4d74',
        };

        let  h3StyleFormSigninHeading = {
            fontFamily: "'Marck Script', cursive",
            color: '#0c4d74',
        };

        return(
            <div className="modal fade" id="blogModal"  tabIndex="-1" role="dialog" aria-hidden="true">
                <div className="modal-dialog">
                    <div className="modal-content" style={divStyleModalContent}>
                        <div className="modal-header">
                            <button type="button" className="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                            <h4 className="modal-title" style={h4StyleModalTitle}>Вход на сайт</h4>
                        </div>
                        <div className="modal-body">
                            <form className="form-signin" id='loginForm' role="form" onSubmit={this.checkLogin}>
                                <h3 className="form-signin-heading" style={h3StyleFormSigninHeading}>Введите свои данные:</h3>
                                <input type="text" className="form-control" placeholder="Логин" required/>
                                <input type="password" className="form-control" placeholder="Пароль" required/>
                                <button className="btn btn-lg btn-block btn-info" type="submit">Войти</button>
                            </form>
                        </div>
                        <div className="modal-footer">
                            <button type="button" className="btn btn-info" data-dismiss="modal">Закрыть</button>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

Modal.contextTypes = {
     router: React.PropTypes.object.isRequired
 };