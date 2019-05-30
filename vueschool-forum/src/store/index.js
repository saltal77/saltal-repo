import Vue from 'vue';
import Vuex from 'vuex';
import sourceData from '@/data';

Vue.use(Vuex);

export default new Vuex.Store({
  //state: sourceData,

  state: {
    ...sourceData,
    authId: 'VXjpr2WHa8Ux4Bnggym8QFLdv5C3', //batman Id
  },

  getters: {
    authUser (state) {
      return state.users[state.authId]
    },
  },

  actions:{
    createPost (context, post) {
      const postId = 'greatPost' + Math.random();
      post['.key'] = postId;
      context.commit('setPost', {post, postId});
      context.commit('appendPostToThread', {threadId: post.threadId, postId });
      context.commit('appendPostToUser', {userId: post.userId, postId })
    },
  },

  mutations: {
    setPost(state,  {post, postId}) {
      // Vue.set(this.$store.state.posts, postId, post);
      Vue.set(state.posts, postId, post);
    },
    appendPostToThread(state, {postId, threadId}) {
      // Vue.set(this.thread.posts, postId, postId);
      const thread = state.threads[threadId];
      Vue.set(thread.posts, postId, postId);
    },
    appendPostToUser(state, {postId, userId}) {
      // Vue.set(this.$store.state.users[post.userId].posts, postId, postId)
      const user = state.users[userId];
      Vue.set(user.posts, postId, postId)
    },

  },

});
