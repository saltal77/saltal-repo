<template>
    <div>
          <div class="avatar">
            <a href="#">
              <img  :src="user.avatar">
            </a>
            <p><b>{{user.name}}</b></p>
            <p>{{userPostCount}} posts</p>
            <!--<p> {{(users[posts[postId].userId].posts)}}</p>-->
          </div>
          <div>
            <p>{{post.text}}</p>
          </div>
      <div>
        <AppDate :timestamp="post.publishedAt"/>
      </div>
          <!--<div :title="post.publishedAt | humanFriendlyDate">-->
            <!--<p>{{ post.publishedAt | diffForHumans }}</p>-->
          <!--</div>-->
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
        post: {
          required: true,
          type: Object,

        }
      },
      computed: {
        user () {
          return this.$store.state.users[this.post.userId]
        },
        userPostCount() {
          //return Object.keys(this.user.posts).length
          return countObjectproperties(this.user.posts)
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
