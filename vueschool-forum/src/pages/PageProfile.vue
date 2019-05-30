<template>
  <div>
    <div>
      <img :src="user.avatar">
      <h4>{{user.username}}</h4>
      <p>{{user.name}}</p>
      <p>
        <span v-if="user.bio">{{user.bio}}</span>
        <span v-else>No bio provided</span>
      </p>
      <p>
        <span>{{user.username}} is online</span>
      </p>
    </div>
    <div>
      <span> {{userPostsCount}} posts</span>
      <span> {{userThreadsCount}} threads</span>
    </div>
    <div>
      <span v-if="user.website">
        <a :href="user.website">{{user.website}}</a>
      </span>
    </div>
    <div>
      <PostList :posts="userPosts"/>
    </div>

  </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import PostList from "../components/PostList";
    import {countObjectproperties} from '@/utils'

    export default {
      components: {PostList},
      computed: {
        ...mapGetters({
          user: 'authUser'
        }),
        userPostsCount() {
          //return this.user.posts ? Object.keys(this.user.posts).length : 0
          return countObjectproperties(this.user.posts)

        },
        userThreadsCount() {
          //return this.user.threads ? Object.keys(this.user.threads).length : 0
          return  countObjectproperties(this.user.threads)
        },
        userPosts () {
          if (this.user.posts) {
            return Object.values(this.$store.state.posts)
              .filter(post => post.userId === this.user['.key'])
          }
          return []
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
