<template>
  <div>
    <div>
      <h3> {{thread.title}}</h3>
      <span>by User <AppDate :timestamp="thread.publishedAt"/></span>
    </div>
    <div>
      <PostList :posts="posts"/>
    </div>
    <!--event listener-->
    <!--<PostEditor @save="addPost" :threadId="id"/>-->
     <PostEditor :threadId="id"/>
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
  //import Vue from 'vue';
  import PostList from '@/components/PostList'
  import PostEditor from '@/components/PostEditor'

  export default {
    name: 'PageThreadShow',
    components : {
      PostList,
      PostEditor,
    },
    props: {
      id: {
        required: true,
        type: String,
      },
    },
    data () {
      return {
         thread: this.$store.state.threads[this.id],
         // posts: this.$store.state.posts,
         // users: this.$store.state.users,
        //newPostText: '',
      }
    },
    computed: {
      posts () {
        const postIds = Object.values(this.thread.posts);
        return Object.values(this.$store.state.posts)
          .filter(post => postIds.includes(post['.key']))
      }
    },
    methods: {
        //addPost(eventData) {
        //console.log(eventData)
        //const post = eventData.post
        //const postId = eventData.post['.key']
        //деструктурирующее присваивание {post} - поступает объект eventData с ключом post ...
       // addPost({post}) {
         // const postId = post['.key'];
        // Vue.set(obj, propertyName, value)
        // this.$set(obj, propertyName, value)
        // this.$set(this.$store.state.posts, postId, post);
        // this.$set(this.thread.posts, postId, postId);
        // this.$set(this.$store.state.users[post.userId].posts, postId, postId)
      //}
    }
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
