# QE-C Backlog Status

**Latest Run:** 2026-02-15 23:52:46 GMT
*(Please refresh to see latest results)*

This is the dashboard for Quality Engineering for Containers, Images and Public Cloud.

We are currently working on four projects: Containers & Images and Public Cloud
* [General team overview](#general_team_overview)
  * [Bugs vs Features Backlog Length](#bugs_vs_features_backlog_length)
  * [Incoming vs outcoming during the last 30 days](#incoming_vs_outcoming_during_the_last_30_days)
  * [Incoming vs outcoming during the last 4 months](#incoming_vs_outcoming_during_the_last_4_months)
* [Backlog Lengths by priority](#backlog_lengths_by_priority)
* [Pickup time alerts](#pickup_time_alerts)
* [Non updated tickets for 15 days](#non_updated_tickets_for_15_days)
  * [Tickets in progress with no changes in 15 days](#tickets_in_progress_with_no_changes_in_15_days)
  * [Tickets with the status Blocked and Feedback with no changes in 15 days](#tickets_with_the_status_blocked_and_feedback_with_no_changes_in_15_days)
* [No Changes in 15 Days (Blocked and Feedback)](#no_changes_in_15_days_blocked_and_feedback)
* [Abnormalities](#abnormalities)
  * [In Progress But Not Assigned](#in_progress_but_not_assigned)
  * [Assigned but not started](#assigned_but_not_started)
  * [New tickets](#new_tickets)
  * [Coordination without subtasks](#coordination_without_subtasks)
* [Epics](#epics)

# General team overview <a name='general_team_overview'></a>
**Bugs vs Features Backlog Length <a name='bugs_vs_features_backlog_length'></a>**

This table compares the number of bugs against the planned tickets.          

Project | Bugs | Features | Total
--- | --- | --- | ---
 | Containers & Images | [ 0 (0%) ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%3D&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 121 (100%) ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%21&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 121 ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&v%5Bstatus_id%5D%5B%5D=2&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=)
 | Public Cloud | [ 0 ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=5&v%5Bstatus_id%5D%5B%5D=6&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Et-&v%5Bcreated_on%5D%5B%5D=30&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | [ 0 ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=closed_on&op%5Bclosed_on%5D=%3Et-&v%5Bclosed_on%5D%5B%5D=30&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | [ 0 ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&v%5Bstatus_id%5D%5B%5D=2&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | &#x1F49A;


**Incoming vs outcoming during the last 4 months <a name='incoming_vs_outcoming_during_the_last_4_months'></a>**

Backlog Query | New tickets | Finished tickets | Backlog length | Status
--- | --- | --- | --- | ---
 | Containers | [ 156 ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=5&v%5Bstatus_id%5D%5B%5D=6&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Et-&v%5Bcreated_on%5D%5B%5D=120&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | [ 161 ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=closed_on&op%5Bclosed_on%5D=%3Et-&v%5Bclosed_on%5D%5B%5D=120&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | [ 121 ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&v%5Bstatus_id%5D%5B%5D=2&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | &#x1F49A;
 | Public Cloud | [ 0 ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=5&v%5Bstatus_id%5D%5B%5D=6&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Et-&v%5Bcreated_on%5D%5B%5D=120&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | [ 0 ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=closed_on&op%5Bclosed_on%5D=%3Et-&v%5Bclosed_on%5D%5B%5D=120&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | [ 0 ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&v%5Bstatus_id%5D%5B%5D=2&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | &#x1F49A;



# Backlog Lengths by priority <a name='backlog_lengths_by_priority'></a>
These tables show the backlog length per priority. The "Warning level" is a the max number of tickets that we consider safe. This level is established by consensus in the team.

**Containers <a name='containers'></a>**

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Urgent Priority Length: Containers & Images ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 1 | &#x1F49A;
 | [ High Priority Length: Containers & Images ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 4 | 3 | &#x1F534;
 | [ Normal Priority Length: Containers & Images ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 9 | 20 | &#x1F49A;


**Public Cloud <a name='public_cloud'></a>**

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Urgent Priority Length: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 1 | &#x1F49A;
 | [ High Priority Length: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 3 | &#x1F49A;
 | [ Normal Priority Length: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 20 | &#x1F49A;



# Pickup time alerts <a name='pickup_time_alerts'></a>
These tables show the tickets that are in violation of the [SLO](https://progress.opensuse.org/projects/openqatests/wiki#SLOs-service-level-objectives)

**Urgent Priority <a name='urgent_priority'></a>**

Backlog Query | Number of issues | Status
--- | --- | ---
 | [ Urgent Priority: Containers & Images ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=7&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=assigned_to&c%5B%5D=fixed_version&c%5B%5D=is_private&c%5B%5D=due_date&c%5B%5D=relations&c%5B%5D=priority&group_by=&t%5B%5D=) | 0 | &#x1F49A;
 | [ Urgent Priority: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=7&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | &#x1F49A;


**High Priority <a name='high_priority'></a>**

Backlog Query | Number of issues | Status
--- | --- | ---
 | [ High Priority: Containers & Images ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=30&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 1 | &#x1F534;
 | [ High Priority: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=30&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | &#x1F49A;


 | [ Normal Priority: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=365&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | &#x1F49A;



# Non updated tickets for 15 days <a name='non_updated_tickets_for_15_days'></a>
These tables show the tickets that have more than 15 days without any update

**Tickets in progress with no changes in 15 days <a name='tickets_in_progress_with_no_changes_in_15_days'></a>**

These tickets are in progress and we should review that because maybe have blockers or are under feedback and we forgot to update the status of the ticket.

Backlog Query | Number of issues | Status
--- | --- | ---
 | [ Not Changed: Containers & Images ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 10 | &#x1F534;
 | [ Not Changed: Public Cloud ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | &#x1F49A;


**Tickets with the status Blocked and Feedback with no changes in 15 days <a name='tickets_with_the_status_blocked_and_feedback_with_no_changes_in_15_days'></a>**

These tickets are in progress and we should review that because maybe what is blocking is solved. Or we need to insist when we don't have feedback.

Backlog Query | Number of issues | Status
--- | --- | ---
 | [ Not Changed: Containers & Images (Blocked and Feedback) ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 17 | &#x1F534;
 | [ Not Changed: Public Cloud (Blocked and Feedback) ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | &#x1F49A;



# Abnormalities <a name='abnormalities'></a>
These tickets has some kind of abnormality, and should be alerted to the team and reviewed

**In Progress But Not Assigned <a name='in_progress_but_not_assigned'></a>**

These are the typical tickets that due to forgetfulness are in progress but there is no assigned person. 
If there is any clarification to be made with the person who is working with it, we need to know his name

Backlog Query | Number of issues | Status
--- | --- | ---
 | [ Not Assigned: Containers & Images ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=%21*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 1 | &#x1F534;
 | [ Not Assigned: Public Cloud ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=%21*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | &#x1F49A;


**Assigned but not started <a name='assigned_but_not_started'></a>**

Some tickets could be blocked by a teammate for a time assigned to him but not started. This option is considered, 
but care must be taken if too much time has passed or if the person is on sick leave or on vacation. 
This would mean that the task is effectively blocked

Backlog Query | Number of issues | Status
--- | --- | ---
 | [ Assigned but not started: Containers & Images ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 4 | &#x1F534;
 | [ Assigned but not started: Public Cloud ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | &#x1F49A;


**New tickets <a name='new_tickets'></a>**

New tickets that are not workable and need clarification should be reviewed during the refinement meeting.

Backlog Query | Number of issues | Status
--- | --- | ---
 | [ New: Containers & Images ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=assigned_to&c%5B%5D=fixed_version&c%5B%5D=is_private&c%5B%5D=due_date&c%5B%5D=relations&c%5B%5D=priority&group_by=&t%5B%5D=) | 54 | &#x1f448;
 | [ New: Public Cloud ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 


**Coordination without subtasks <a name='coordination_without_subtasks'></a>**

Epics can be defined to record a new line of work in a project. 
Initially these epics may not have tasks assigned to them. This table is a reminder for the PO

Backlog Query | Number of issues | Status
--- | --- | ---
 | [ Coordination with no subtasks: Containers & Images ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=6&f%5B%5D=child_id&op%5Bchild_id%5D=%21*&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=3&v%5Bstatus_id%5D%5B%5D=5&v%5Bstatus_id%5D%5B%5D=6&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | &#x1F49A;
 | [ Coordination with no subtasks: Public Cloud ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=6&f%5B%5D=child_id&op%5Bchild_id%5D=%21*&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=3&v%5Bstatus_id%5D%5B%5D=5&v%5Bstatus_id%5D%5B%5D=6&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | &#x1F49A;



# Epics <a name='epics'></a>
**Container & Images Epics <a name='container_&_images_epics'></a>**

Epic | Status | Start Date | Progress
--- | --- | --- | ---
 | [ Testing of the SLES 16.1 transactional mode](https://progress.opensuse.org/issues/195287) | New | 2026-01-22 | 33%
 | [{Publiccloud} Azure AITL/LISA testing](https://progress.opensuse.org/issues/193213) | New | 2024-10-17 | 66%
 | [{Publiccloud} Establish disaster recover for larry...](https://progress.opensuse.org/issues/192139) | New | 2025-11-06 | 0%
 | [{Publiccloud} Application images](https://progress.opensuse.org/issues/191374) | New | 2025-09-10 | 100%
 | [{WSL} Switch to a semi-automatic model](https://progress.opensuse.org/issues/190269) | New | 2025-10-16 | 42%
 | [ SLES 16 Maintenance for QE-C](https://progress.opensuse.org/issues/189015) | New | 2025-08-06 | 88%
 | [ Infrastructure monitoring project](https://progress.opensuse.org/issues/186612) | New | 2024-10-24 | 90%
 | [{WSL} Test images before release](https://progress.opensuse.org/issues/186594) | New | 2025-04-10 | 100%
 | [{retro} Instable tests, avoid repetitive workload](https://progress.opensuse.org/issues/186543) | New | 2025-07-30 | 0%
 | [{retro} PR Management](https://progress.opensuse.org/issues/186537) | New | 2025-07-30 | 0%
 | [{PublicCloud} Knowledge democratization of the Pub...](https://progress.opensuse.org/issues/185323) | New | 2022-08-08 | 62%
 | [{Publiccloud} Use CloudCustodian as resource guardian](https://progress.opensuse.org/issues/182825) | New | 2025-05-22 | 44%
 | [{Publiccloud} DMS testing](https://progress.opensuse.org/issues/177093) | New | 2025-02-13 | 66%
 | [Public Cloud Documentation](https://progress.opensuse.org/issues/116947) | New | 2022-09-22 | 66%
 | [{WSL} WSL Documentation](https://progress.opensuse.org/issues/116944) | New | 2022-09-21 | 0%
 | [{MinimalVM} MinimalVM Cloud image test automation](https://progress.opensuse.org/issues/107446) | New | 2020-04-29 | 90%
 | [{Publiccloud} Test Maintenance images](https://progress.opensuse.org/issues/107200) | New | 2022-02-21 | 90%
 | [{MinimalVM} separate hyperv from svirt backend](https://progress.opensuse.org/issues/95422) | New | 2025-07-25 | 0%


**Public Cloud Epics <a name='public_cloud_epics'></a>**



No active epics for this project


# Aging of tickets <a name='aging_of_tickets'></a>
Mesures the time since the ticket is created and the ticket is resolved

**Aging tickets finished in the last 30 days <a name='aging_tickets_finished_in_the_last_30_days'></a>**

Backlog Query | Days to complete (Adv) | Days to complete (Median) | Days to complete (Std deviation)
--- | --- | --- | ---
 | [ Containers & Images ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=closed_on&op%5Bclosed_on%5D=%3Et-&v%5Bclosed_on%5D%5B%5D=30&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 41 | 16 | 10
# Other links

**Finished tickets this week**
* [Containers & Images](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=closed_on&op%5Bclosed_on%5D=w&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=)
* [Public Cloud](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=closed_on&op%5Bclosed_on%5D=w&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=)
