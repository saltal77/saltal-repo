<template>
      <span :title="timestamp | humanFriendlyDate">{{ timestamp | diffForHumans }}.</span>
</template>
<script>
  import moment from 'moment'

  export default {
      props: {
          timestamp: {
            reqired: true,
            type: Number,
            default: 1977345679,
          }
      },
        filters: {
        humanFriendlyDate (date) {
          return moment.unix(date).format('MMMM Do YYYY, h:mm:ss a') // .unix(date).locale('ru')
        },
        diffForHumans(date) {
          return moment.unix(date).fromNow()
        },
      }
    }
</script>
<style scoped>

</style>
