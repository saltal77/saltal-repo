<template>
    <div>
      <PostListItem
        v-for="post in posts"
        :post="post"
        :key="post['.key']"
      />
      <!--<div v-for="postId in thread.posts">-->
        <!--<div class="avatar">-->

          <!--<a href="#">-->
            <!--<img  :src="users[posts[postId].userId].avatar">-->
          <!--</a>-->
          <!--<p><b>{{users[posts[postId].userId].name}}</b></p>-->
          <!--&lt;!&ndash;<p> {{(users[posts[postId].userId].posts)}}</p>&ndash;&gt;-->

        <!--</div>-->
        <!--<div>-->

          <!--<p>{{posts[postId].text}}</p>-->
        <!--</div>-->
        <!--<div>-->
          <!--<p>{{posts[postId].publishedAt}}</p>-->
        <!--</div>-->

      <!--</div>-->
    </div>
</template>

<script>
  import PostListItem from './PostListItem'

  export default {
    components: {
      PostListItem
    },
    props: {
        posts: {
          required: true,
          type: Array,
        }
      }
    }
</script>
<style scoped>

</style>
