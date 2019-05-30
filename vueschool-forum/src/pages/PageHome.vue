<template>
  <div>
    <h1>Welcome to Forum</h1>
    <CategoryList :categories="categories"/>
    <!--<div v-for="thread in threads">-->
      <!--<div>-->
        <!--<h4> {{thread.title}}</h4>-->
      <!--</div>-->
        <!--<div v-for="postId in thread.posts">-->
          <!--<div class="avatar">-->
            <!--<a href="#">-->
              <!--<img  :src="users[posts[postId].userId].avatar">-->
            <!--</a>-->
          <!--</div>-->
          <!--<div>-->
            <!--<p>{{users[posts[postId].userId].name}}</p>-->
            <!--<p>{{posts[postId].text}}</p>-->
          <!--</div>-->
        <!--</div>-->
    <!--</div>-->
  </div>
</template>
<script>
  import CategoryList from "../components/CategoryList";

  export default {
    name: 'PageHome',
    components: {
      CategoryList,
    },
    computed: {
      categories() {
        return Object.values(this.$store.state.categories)
      }
    },
    // data () {
    //   return {
    //     //categories: Object.values(this.$store.state.categories),
    //     // posts: this.$store.state.posts,
    //     // users: this.$store.state.users,
    //   }
    // }
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  img {
    float: left;
    width: 100px;
    height: 100px;
    border-radius: 50%;
  }
</style>
