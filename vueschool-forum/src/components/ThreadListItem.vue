<template>
  <div>
    <div>
      <p>
        <!--<a :href="`/thread/${thread['.key']}`">{{thread.title}}</a>-->
        <!--<router-link :to="`/thread/${thread['.key']}`">-->
          <!--{{thread.title}}-->
        <!--</router-link>-->
        <router-link :to="{name: 'PageThreadShow', params: {id: thread['.key']} }">
          {{thread.title}}
        </router-link>
      </p>
      <p>
        by {{user.name}} <AppDate :timestamp="thread.publishedAt"/></p>
    </div>
    <div>
      <p>
        {{repliesCount}} {{repliesCount === 1 ? 'reply' : 'replies'}}
      </p>
      <img :src="user.avatar">
    </div>
  </div>
</template>

<script>
  //import AppDate from './AppDate';
  import {countObjectproperties} from '@/utils'

  export default {
    // components: {
    //   AppDate,
    // },

    props: {
      thread: {
        required: true,
        type: Object
      },
    },
    computed: {
      repliesCount() {
        //return Object.keys(this.thread.posts).length - 1
        return countObjectproperties(this.thread.posts) - 1
      },
      user() {
        return this.$store.state.users[this.thread.userId]
      },
    },
  }
</script>
<style scoped>
  img {
    float: left;
    width: 100px;
    height: 100px;
    border-radius: 50%;
  }
</style>
