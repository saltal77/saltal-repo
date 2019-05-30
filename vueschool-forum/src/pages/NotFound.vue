<template>
  <div>
     <h2 :class="$style['heading-large']">Not found - 404</h2>
    <p :class="$style.textLarge">We cant find this page...</p>
    <router-link :to="{name : 'Home'}">
      go home?
    </router-link>
  </div>
</template>

<script>
  // $vm0.$style.textLarge - получим доступ
export default {
  name: 'PageNotFound',
}
</script>
<style module>
  .heading-large { font-size: 75px; }
  .textLarge {  font-size: 50px; font-weight: 100; }
</style>
