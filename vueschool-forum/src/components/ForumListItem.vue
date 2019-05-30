<template>
    <div>
      <div><router-link :to="{name: 'Forum', params: {id: forum['.key']}}">
        {{forum.name}}
      </router-link>
      </div>
      <div>
        <span class="desc">{{forum.description }}</span>
        <span>{{threadsCount}} {{threadsCount === 1 ? 'thread' : 'threads'}}</span>
      </div>
    </div>
</template>
<script>
    import {countObjectproperties} from '@/utils'
    export default {
      name: "ForumListItem",
      props: {
          forum: {
            reqired: true,
            type: Object,
          }
      },
      computed: {
          threadsCount () {
            //return this.forum.threads ? Object.values(this.forum.threads).length : 0
            return countObjectproperties(this.forum.threads)
          }
       }
    }
</script>
<style scoped>

</style>
