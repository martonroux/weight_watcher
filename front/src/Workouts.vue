<script setup>
import WorkoutWidget from "@/components/workout/WorkoutWidget.vue";
</script>

<template>
  <div class="main-workout">
    <ol>
      <li v-for="(wrkt, index) in listWorkouts" :key="index">
        <WorkoutWidget :wrkt-data="wrkt" class="widget"/>
      </li>
    </ol>
  </div>
</template>

<script>
import { fetchWorkouts } from "@/js_components/get_requests";

export default {
  data () {
    return {
      listWorkouts: []
    }
  },
  mounted () {
    fetchWorkouts().then(result => {
      this.listWorkouts = result['data'];
    });
  }
}
</script>

<style scoped>

.main-workout {
  overflow-x: hidden;
}

</style>