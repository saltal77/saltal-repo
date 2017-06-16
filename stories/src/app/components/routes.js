import React from 'react'
import { Route, IndexRoute, Redirect} from 'react-router';

import Blog from '../layouts/BlogLayout';
import about from '../pages/About';
import interest from '../pages/Interest';
import contacts from '../pages/Contacts';
import comments from '../pages/Comments'
import Main from '../pages/Main'
import AuthorInfo from './AuthorInfo'
import NotFound from '../pages/notFound404'


module.exports = (

<Route path="/" component={Blog}>
    <IndexRoute component={Main} />
    <Route path='about' component={about} >
        <Route path=":authorId" component={AuthorInfo} />
    </Route>
    <Route path='interest' component={interest} />
    <Route path='contacts' component={contacts} />
    <Route path='comments' component={comments} />
    <Redirect from='/redirect' to="/" />
    <Route path='*' component={NotFound} />
</Route>

);