<template>
  <header>
    <router-link :to="{name: 'Home'}">
      <img src="../assets/logo.png">
    </router-link>
    <nav>
      <ul>
        <li>
          <router-link :to="{name: 'Profile'}">
            <img :src="user.avatar">
            <span>{{user.name}}</span>
          </router-link>
          </a>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script>
    import {mapGetters} from 'vuex';
    export default {
        name: "TheNavbar",
        computed: {
          ...mapGetters({
            'user': 'authUser'
          })
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
