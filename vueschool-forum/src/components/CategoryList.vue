<template>
  <div>
    <CategoryListItem
      v-for="category in categories"
      :category="category"
      :key="category['.key']"
     />
  </div>
</template>

<script>
  import CategoryListItem from './CategoryListItem'

  export default {
      name: "CategoryList",
      components: {CategoryListItem},
      props: {
          categories: {
            reqired: true,
            type: Array,
          }
       }
    }
</script>
<style scoped>

</style>
