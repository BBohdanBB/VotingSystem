from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from polls.models import Post, Candidate
from polls.forms import PostForm, CandidateFormHelper, CandidateFormset
from django.contrib.auth.decorators import login_required


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'polls/addpost_tmp.html'
    model = Post
    success_url = '/'


    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        candidate_form = CandidateFormset()
        candidate_formhelper = CandidateFormHelper()

        return self.render_to_response(
            self.get_context_data(form=form, candidate_form=candidate_form)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        candidate_form = CandidateFormset(self.request.POST, request.FILES)

        if (form.is_valid() and candidate_form.is_valid()):
            return self.form_valid(form, candidate_form)

        return self.form_invalid(form, candidate_form)

    def form_valid(self, form, candidate_form):
        """
        Called if all forms are valid. Creates a Author instance along
        with associated books and then redirects to a success page.
        """
        self.object = form.save()
        candidate_form.instance = self.object
        candidate_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, candidate_form):
        """
        Called if whether a form is invalid. Re-renders the context
        data with the data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, candidate_form=candidate_form)
        )

    def get_context_data(self, **kwargs):
        """ Add formset and formhelper to the context_data. """
        ctx = super(PostCreateView, self).get_context_data(**kwargs)
        candidate_formhelper = CandidateFormHelper()

        if self.request.POST:
            ctx['form'] = PostForm(self.request.POST, self.request.FILES)
            ctx['candidate_form'] = CandidateFormset(self.request.POST)
            ctx['candidate_formhelper'] = candidate_formhelper
        else:
            ctx['form'] = PostForm()
            ctx['candidate_form'] = CandidateFormset()
            ctx['candidate_formhelper'] = candidate_formhelper

        return ctx
