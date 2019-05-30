<template>
    <form @submit.prevent="save">
        <div>
          <textarea
            name=""
            rows="10"
            cols="30"
            v-model="text"
          >
          </textarea>
        </div>
        <div>
          <button>Submit</button>
        </div>
      </form>
</template>
<script>
    export default {
      props: {
        threadId: {
          requires: true,
        }
      },
      data() {
          return {
            text: ''
          }
      },
      methods: {
        save () {
          // const moved to store
          //const postId = 'greatPost' + Math.random();
        const post = {
          text: this.text,
          publishedAt: Math.floor(Date.now() /1000),
          threadId: this.threadId,
          userId: 'L664y3qZSubDbT1R6npC0EEybJ73', // Mr.Burns Id
        };
        this.text = '';
        this.$emit('save', {post});
        this.$store.dispatch('createPost', post );
        },
      },
    }
</script>
<style scoped>

</style>
