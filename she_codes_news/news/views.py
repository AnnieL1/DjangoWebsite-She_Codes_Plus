from django.views import generic
from .models import NewsStory
from django.urls import reverse_lazy
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required



class IndexView(generic.ListView):
    # model=NewsStory
    template_name = 'news/index.html'
    # context_object_name = 'latest_stories'

    def get_queryset(self):
        # if self.request.user.is_authenticated:
            # return StoryForm.objects.all()
        # else:
        #     return super().get_queryset()
        return NewsStory.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
    #     # context['latest_stories'] = NewsStory.objects.filter(author__contains='annie')  ## W3 school filter table for functions to use query table 
    #     context['all_stories'] = NewsStory.objects.all().order_by("-pub_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:3]
        context['all_stories'] = NewsStory.objects.all().order_by("-pub_date")
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html' #default: news/newsstory_detail.html
    context_object_name = 'story'  #default: newsstory TIP:USE DEFAULT SO IT'S EASY TO READ AND REMEMBER WHERE IT'S FROM, ESPECIALLY WHEN YOURE SHARING CODE

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    form_class = StoryForm
    # context_object_name = 'storyForm'
    # template_name = 'news/createstory.html'
    template_name = 'news/newsstory_form.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class StoryEditView(generic.UpdateView):
    model = NewsStory
    # form_class = StoryForm
    template_name = 'news/newsstory_form.html'
    fields = ['title','pub_date','content']

    def success_url(self):
        # return super().get_success_url() #super means do what you would do if i haven't told you otherwise, I'll then start modifying from there
        return redirect('news:story',kwargs = {'pk':self.kwargs['pk']})
        # self.kwags['pk'])
    
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated: ## can use LoginRequiredMixin instead of this if not statement
            raise qs.model.DoesNotExist
        qs = qs.filter(author =self.request.user)
        return qs

class StoryDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = NewsStory
    success_url = reverse_lazy('news:index')

    def get_queryset(self):
        '''filter to allow users to ONLY delte their own stories'''
        qs = super().get_queryset()
        # if not self.request.user.is_authenticated:
        #     raise qs.model.DoesNotExist
        return qs.filter(author =self.request.user)

#@login_required
    # def like(request, pk):
    #     '''when given a pk for a news story, add the user to the like, or if exist remove the user'''
    #     news_story = get_object_or_404(pk=pk)
    #     if news_story.fave_by.filter(username=request.users):
    #         news_story.fave_by.remove(request.user)
    #     else:
    #         news_story.fave_by.remove(request.user)
    #     return reverse_lazy("news:story", kwargs={'pk':pk})

