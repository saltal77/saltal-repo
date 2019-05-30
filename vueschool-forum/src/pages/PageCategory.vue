<template>
    <div>
      <h3>{{category.name}}</h3>
      <CategoryListItem :category="category"/>
    </div>
</template>
<script>
  import CategoryListItem from '@/components/CategoryListItem';

  export default {
      components: {CategoryListItem},
      props: {
          id: {
            reqired: true,
            type: String,
          }
      },
      computed: {
          category () {
            return this.$store.state.categories[this.id]
          }
       }
    }
</script>
<style scoped>

</style>
