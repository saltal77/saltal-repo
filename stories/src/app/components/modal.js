import React, { Component } from 'react';


export default class Modal extends Component
{
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
                            <form className="form-signin" role="form">
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
