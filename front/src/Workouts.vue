<script setup>
import WorkoutWidget from "@/components/widgets/WorkoutWidget.vue";
</script>

<template>
  <li v-for="(wrkt, index) in listWorkouts" :key="index">
    <WorkoutWidget :wrkt-data="wrkt" class="widget"/>
  </li>
</template>

<script>
import { fetchWorkouts } from "@/js_components/requests";

export default {
  data () {
    return {
      listWorkouts: []
    }
  },
  mounted () {
    fetchWorkouts().then(result => {
      console.log(result);
      this.listWorkouts = result['data'];
    });
  }
}
</script>

<style scoped>

</style>