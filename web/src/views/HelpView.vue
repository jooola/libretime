<script setup lang="ts">
import { projectDocumentationUrl, projectForumUrl } from '@/constants'
</script>

<template>
  <div>
    <h2>
      {{ $t('views.HelpView.title') }}
    </h2>
    <p>{{ $t('views.HelpView.steps') }}</p>

    <div>
      <v-timeline
        side="end"
        truncate-line="both"
      >
        <v-timeline-item
          v-for="[title, text] in [
            [
              $t('views.HelpView.steps-upload-tracks'),
              $t('views.HelpView.steps-upload-tracks-help')
            ],
            [
              $t('views.HelpView.steps-schedule-show'),
              $t('views.HelpView.steps-schedule-show-help')
            ],
            [
              $t('views.HelpView.steps-add-tracks-show'),
              $t('views.HelpView.steps-add-tracks-show-help')
            ]
          ]"
          density="compact"
          size="small"
        >
          <v-card>
            <v-card-title>{{ title }}</v-card-title>
            <v-card-text>{{ text }}</v-card-text>
          </v-card>
        </v-timeline-item>
      </v-timeline>
    </div>

    <p>
      <i18n-t keypath="views.HelpView.steps-documentation">
        <template v-slot:documentation>
          <a
            :href="projectDocumentationUrl"
            target="_blank"
            rel="noopener noreferrer"
            >{{ $t('views.HelpView.steps-documentation-link') }}</a
          >
        </template>
      </i18n-t>
    </p>
  </div>
</template>
