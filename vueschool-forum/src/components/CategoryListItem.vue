<template>
   <div>
    <h3>
     <router-link :to="{name: 'Category', params: {id: category['.key']}}">
       {{category.name}}
     </router-link>
    </h3>
    <ForumList :forums="categoryForums"/>
  </div>
</template>
<script>
  import ForumList from './ForumList'

  export default {
      name: "CategoryListItem",
      components: {ForumList},
      props: {
          category: {
            reqired: true,
            type: Object,
          }
      },
      computed: {
          categoryForums () {
            return Object.values(this.$store.state.forums)
              .filter(forum => forum.categoryId === this.category['.key'])
          }
       },
    }
</script>
<style scoped>

</style>
