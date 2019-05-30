<template>
  <div>
    <div>
      <h4>{{forum.name}}</h4>
      <p> {{forum.description}} </p>
    </div>
    <ThreadList :threads="threads"/>
  </div>
</template>
<script>
    import ThreadList from "@/components/ThreadList";

    export default {
      name: "PageForum",
      components: {ThreadList},
      props: {
          id: {
            required: true,
            type: String,
          },
      },
      computed: {
        forum () {
            return this.$store.state.forums[this.id]
          },
        threads () {
            return Object.values(this.$store.state.threads)
              .filter(thread => thread.forumId === this.id)
        }
      }
    }
</script>
<style scoped>

</style>
