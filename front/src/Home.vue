<script setup>
import StatsWidget from "./components/widgets/StatsWidget.vue";
import ActiveWorkoutWidget from "@/components/widgets/ActiveWorkoutWidget.vue";
</script>

<template>
  <div class="widget-container">
    <ActiveWorkoutWidget v-if="activeWorkout['id'] !== -1" :workout="activeWorkout" @end-workout="endWorkout"/>
    <StatsWidget :growth-percent="growthPercent" :additional-text="': body weight'"/>
    <StatsWidget :growth-percent="firstValue" :additional-text="': workout weight'"/>
  </div>
</template>

<script>
import {fetchActiveWorkout, fetchBodyWeights} from "@/js_components/get_requests";

export default {
  data() {
    return {
      growthPercent: 0,
      firstValue: 0,
      activeWorkout: {}
    }
  },
  mounted() {
    fetchBodyWeights().then(result => {
      if (result["error"] === true) {
        this.growthPercent = NaN;
        this.firstValue = NaN;
      } else {
        this.growthPercent = result['data']['evolution'].toFixed(2);
        this.firstValue = result['data']['average'].toFixed(2);
      }
    });
    fetchActiveWorkout().then(result => {
      this.activeWorkout = result;
    });
  },
  methods: {
    endWorkout() {
      this.activeWorkout['id'] = -1;
    }
  }
}
</script>

<style scoped>

.widget-container {
  display: flex;
  flex-direction: column;
}

</style>
