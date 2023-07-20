<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div v-if="open" class="popup-window">
    <div class="popup-content">
      <slot></slot>
    </div>
    <div class="row-div">
      <Button :text="okText" :style="{'background-color': (okText !== 'OK') ? 'gray' : 'var(--accentuation-color)'}" @clicked="closePopup(true)"/>
      <Button :text="'Cancel'" @clicked="closePopup(false)" v-if="!onlyOk"/>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      okText: 'OK'
    }
  },
  props: {
    open: {
      type: Boolean,
      required: true
    },
    timer: {
      type: Boolean,
      required: false
    },
    onlyOk: {
      type: Boolean,
      required: false
    }
  },
  emits: ['closed'],
  watch: {
    open: function (newValue, oldValue) {
      this.countDown(newValue);
    }
  },
  methods: {
    closePopup(isOk) {
      if (isOk === true && this.okText !== 'OK')
        return;

      setTimeout(() => {
        this.$emit('closed', isOk);
      }, 50);
    },
    countDown(newValue) {
      if (this.timer && newValue === true) {
        if (this.okText === '1') {
          this.okText = 'OK';
        } else {
          if (this.okText === 'OK') {
            this.okText = '5';
          } else {
            const num = parseInt(this.okText);
            this.okText = (num - 1).toString();
          }
          setTimeout(() => this.countDown(newValue), 1000);
        }
      }
    }
  },
};
</script>

<style scoped>
.popup-window {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 10000;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;

  :not(:last-child) {
    margin-right: 10px;
  }
}

.row-div {
  display: flex;
  flex-direction: row;
}

.popup-content {
  background-color: var(--widget-color);
  padding: 20px;
  border-radius: var(--widget-border-radius);
}

@media (max-width: 600px) {
  .popup-window {
    flex-direction: column;

    :not(:last-child) {
      margin-right: 0;
    }
  }

  .row-div {
    margin-top: 10px;

    :not(:last-child) {
      margin-right: 10px;
    }
  }
}

@media (max-width: 350px) {
  .popup-content {
    width: 80vw;
  }
}

</style>