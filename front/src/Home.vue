<script setup>
import StatsWidget from "./components/widgets/StatsWidget.vue";
</script>

<template>
  <div class="widget-container">
    <StatsWidget :growth-percent="growthPercent" :additional-text="': body weight'"/>
    <StatsWidget :growth-percent="firstValue" :additional-text="': workout weight'"/>
  </div>
</template>

<script>
import { fetchBodyWeights } from "@/js_components/get_requests";

export default {
  data() {
    return {
      growthPercent: 0,
      firstValue: 0
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
  }
}
</script>

<style scoped>

.widget-container {
  display: flex;
  flex-direction: column;
}

</style>
