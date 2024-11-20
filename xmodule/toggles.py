"""
Add Django settings flags to roll out the extracted XBlocks.
Flags will use to toggle between the old and new block quickly
without putting course content or user state at risk.

Ticket: https://github.com/openedx/edx-platform/issues/35308
"""

# .. toggle_name: USE_EXTRACTED_WORD_CLOUD_BLOCK
# .. toggle_default: False
# .. toggle_implementation: DjangoSetting
# .. toggle_description: Enables the use of the extracted Word Cloud XBlock, which has been shifted to the 'openedx/xblocks-contrib' repo.
# .. toggle_use_cases: temporary
# .. toggle_warning: Not production-ready until https://github.com/openedx/edx-platform/issues/34840 is done.
# .. toggle_creation_date: 2024-11-10
# .. toggle_target_removal_date: 2025-06-01
USE_EXTRACTED_WORD_CLOUD_BLOCK = False

# .. toggle_name: USE_EXTRACTED_ANNOTATABLE_BLOCK
# .. toggle_default: False
# .. toggle_implementation: DjangoSetting
# .. toggle_description: Enables the use of the extracted annotatable XBlock, which has been shifted to the 'openedx/xblocks-contrib' repo.
# .. toggle_use_cases: temporary
# .. toggle_warning: Not production-ready until https://github.com/openedx/edx-platform/issues/34841 is done.
# .. toggle_creation_date: 2024-11-10
# .. toggle_target_removal_date: 2025-06-01
USE_EXTRACTED_ANNOTATABLE_BLOCK = False

# .. toggle_name: USE_EXTRACTED_POLL_QUESTION_BLOCK
# .. toggle_default: False
# .. toggle_implementation: DjangoSetting
# .. toggle_description: Enables the use of the extracted poll question XBlock, which has been shifted to the 'openedx/xblocks-contrib' repo.
# .. toggle_use_cases: temporary
# .. toggle_warning: Not production-ready until https://github.com/openedx/edx-platform/issues/34839 is done.
# .. toggle_creation_date: 2024-11-10
# .. toggle_target_removal_date: 2025-06-01
USE_EXTRACTED_POLL_QUESTION_BLOCK = False

# .. toggle_name: USE_EXTRACTED_LTI_BLOCK
# .. toggle_default: False
# .. toggle_implementation: DjangoSetting
# .. toggle_description: Enables the use of the extracted LTI XBlock, which has been shifted to the 'openedx/xblocks-contrib' repo.
# .. toggle_use_cases: temporary
# .. toggle_warning: Not production-ready until relevant subtask https://github.com/openedx/edx-platform/issues/34827 is done.
# .. toggle_creation_date: 2024-11-10
# .. toggle_target_removal_date: 2025-06-01
USE_EXTRACTED_LTI_BLOCK = False

# .. toggle_name: USE_EXTRACTED_HTML_BLOCK
# .. toggle_default: False
# .. toggle_implementation: DjangoSetting
# .. toggle_description: Enables the use of the extracted HTML XBlock, which has been shifted to the 'openedx/xblocks-contrib' repo.
# .. toggle_use_cases: temporary
# .. toggle_warning: Not production-ready until relevant subtask https://github.com/openedx/edx-platform/issues/34827 is done.
# .. toggle_creation_date: 2024-11-10
# .. toggle_target_removal_date: 2025-06-01
USE_EXTRACTED_HTML_BLOCK = False

# .. toggle_name: USE_EXTRACTED_DISCUSSION_BLOCK
# .. toggle_default: False
# .. toggle_implementation: DjangoSetting
# .. toggle_description: Enables the use of the extracted Discussion XBlock, which has been shifted to the 'openedx/xblocks-contrib' repo.
# .. toggle_use_cases: temporary
# .. toggle_warning: Not production-ready until relevant subtask https://github.com/openedx/edx-platform/issues/34827 is done.
# .. toggle_creation_date: 2024-11-10
# .. toggle_target_removal_date: 2025-06-01
USE_EXTRACTED_DISCUSSION_BLOCK = False

# .. toggle_name: USE_EXTRACTED_PROBLEM_BLOCK
# .. toggle_default: False
# .. toggle_implementation: DjangoSetting
# .. toggle_description: Enables the use of the extracted Problem XBlock, which has been shifted to the 'openedx/xblocks-contrib' repo.
# .. toggle_use_cases: temporary
# .. toggle_warning: Not production-ready until relevant subtask https://github.com/openedx/edx-platform/issues/34827 is done.
# .. toggle_creation_date: 2024-11-10
# .. toggle_target_removal_date: 2025-06-01
USE_EXTRACTED_PROBLEM_BLOCK = False

# .. toggle_name: USE_EXTRACTED_VIDEO_BLOCK
# .. toggle_default: False
# .. toggle_implementation: DjangoSetting
# .. toggle_description: Enables the use of the extracted Video XBlock, which has been shifted to the 'openedx/xblocks-contrib' repo.
# .. toggle_use_cases: temporary
# .. toggle_warning: Not production-ready until relevant subtask https://github.com/openedx/edx-platform/issues/34827 is done.
# .. toggle_creation_date: 2024-11-10
# .. toggle_target_removal_date: 2025-06-01
USE_EXTRACTED_VIDEO_BLOCK = False
