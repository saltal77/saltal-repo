<template>
  <div class="col-full">
    <h3> ThreadList </h3>
      <ThreadListItem
        v-for ="thread in threads"
        :thread="thread"
        :key="thread['.key']"
      />
  </div>
</template>
<script>
  import  ThreadListItem from './ThreadListItem';

  export default {
    name: 'ThreadList',
    components: { ThreadListItem },
    props: {
      threads: {
        required: true,
        type: Array
      },
    },
  }
</script>
<style scoped>

</style>
