<script setup>
import StatsWidget from "./components/widgets/StatsWidget.vue";
</script>

<template>
  <div class="widget-container">
    <StatsWidget :growth-percent="growthPercent"/>
    <StatsWidget :growth-percent="firstValue"/>
  </div>
</template>

<script>
import { fetchWeights } from "@/js_components/requests";

export default {
  data() {
    return {
      growthPercent: 0,
      firstValue: 0
    }
  },
  mounted() {
    fetchWeights().then(result => {
      if (result['error'] === false) {
        this.growthPercent = result['evol_weight'].toFixed(2);
        this.firstValue = result['mean_weight'].toFixed(2);
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
