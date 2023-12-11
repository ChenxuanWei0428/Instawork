from django.shortcuts import render, get_object_or_404, redirect
from .models import TeamMember
from .forms import TeamMemberForm

def team_member_list(request):
    team_members = TeamMember.objects.all()
    total_members = team_members.count()
    return render(request, 'member_page/team_member_list.html', {'team_members': team_members, 'total_members': total_members})


# improve suggestion: currently add and edit page are using the same template since they don't have much different
# but can be seperate in the future for other requirement like for security

def team_member_add(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm()
    return render(request, 'member_page/team_member_form.html', {'form': form})

def team_member_edit(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)

    if request.method == 'POST':
        if 'delete' in request.POST:
            team_member.delete()
            return redirect('team_member_list')
        else:
            form = TeamMemberForm(request.POST, instance=team_member)
            if form.is_valid():
                form.save()
                return redirect('team_member_list')
    else:
        form = TeamMemberForm(instance=team_member)

    return render(request, 'member_page/team_member_form.html', {'form': form, 'team_member': team_member})
