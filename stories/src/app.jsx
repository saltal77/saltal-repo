import React from 'react';
import ReactDOM from 'react-dom';
import routes from './app/components/routes'
import { Router, browserHistory } from 'react-router'

const app = document.getElementById('app');
ReactDOM.render(
    <Router routes={routes} history={browserHistory}/>,
    app
);


// //OLD Routes
// import React from 'react';
// import ReactDOM from 'react-dom';
// import Blog from './app/layouts/BlogLayout';
// import about from './app/pages/About';
// import interest from './app/pages/Interest';
// import contacts from './app/pages/Contacts';
// import comments from './app/pages/Comments'
// import Main from './app/pages/Main'
// import AuthorInfo from './app/components/AuthorInfo'
// import NotFound from './app/pages/notFound404'
//
// import {Router, Route, IndexRoute, browserHistory, Redirect} from 'react-router';
//
// const app = document.getElementById('app');
// ReactDOM.render(
//     <Router history={browserHistory}>
//         <Route path="/" component={Blog}>
//             <IndexRoute component={Main} />
//             <Route path='about' component={about} >
//                 <Route path=":authorId" component={AuthorInfo} />
//             </Route>
//             <Route path='interest' component={interest} />
//             <Route path='contacts' component={contacts} />
//             <Route path='comments' component={comments} />
//         </Route>
//         <Redirect from='/redirect' to="/" />
//         <Route path='*' component={NotFound} />
//     </Router>,
//
//     app
// );
